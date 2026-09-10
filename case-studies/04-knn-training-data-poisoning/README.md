# When a Model Remembers the Attacker Too

*Published: [date] · Companion post: [LinkedIn link] · Illustrative scenario, built from my AI/ML studies*

## What is KNN?

K-Nearest Neighbors (KNN) is one of the simplest ways to teach a computer to recognize things, like handwritten digits. Instead of learning rules, it just remembers every example it was shown. When a new image comes in, it looks at the examples it remembers, finds the ones that look most similar, and copies their answer. No formulas, no training process in the usual sense. Just memory and comparison.

That simplicity is exactly what makes it worth a closer look from a security angle.

## The Scenario

In my AI/ML studies, I built a KNN model that reads handwritten digits, the same kind of technology used in check processing, mail sorting, and form scanning. The assignment focused on accuracy. It didn't ask what happens if someone can quietly add bad examples to what the model remembers.

That question matters because KNN doesn't work like most machine learning models. A neural network has to be retrained before new data changes its behavior, and that retraining is usually a visible, reviewed event. KNN has no such step. It just remembers. The moment someone adds a mislabeled example to its training set, that example is live in production for the very next prediction, no review, no retraining run, nothing to catch in a change log.

I tested this directly. First, I inserted a single copy of a real digit into the training data under the wrong label. The model started misreading that exact digit every time, while its overall accuracy barely moved, less than two tenths of a percent. Nobody watching a dashboard would notice. Then I tried something closer to how a real attacker would operate: instead of one exact copy, I added five slightly altered lookalikes, about 0.4% of the training set. That was enough to make the model misread several real digits it had never seen before, again with almost no change in overall accuracy.

In other words, a handful of bad examples can quietly poison a model's judgment without ever showing up in the numbers everyone actually watches.

## Why This Framework Stack

| Framework | Relevance |
|---|---|
| MITRE ATLAS | This is a training data poisoning technique, an AI specific attack that lives outside traditional IT security. |
| OWASP Top 10 for LLM Applications | LLM05:2026, Data and Model Poisoning. The same pattern OWASP flags for LLMs applies to any model that learns, or in KNN's case remembers, from data that can be updated after launch. |
| NIST AI RMF | The gap sits in the Manage function. Most organizations review a model before it ships, but few review every update to its training data after that. |

## The Solution

This is the part that matters most: this problem is preventable, and it doesn't require exotic tooling. It requires treating training data updates with the same scrutiny as a code change.

**Real tools that already do this:**

- **Cleanlab**, an open source tool built specifically to find mislabeled and suspicious examples in a dataset before they cause harm. It would have caught exactly the kind of poisoned points used in this test.
- **DVC (Data Version Control)**, which lets a team version and roll back training data the same way they version code. If a bad update slips through, you can revert it instead of retraining from scratch.
- **TensorFlow Data Validation (TFDV) and Alibi Detect**, which both catch statistical anomalies and drift in a dataset automatically, flagging the kind of small, suspicious cluster of examples this attack relies on.

None of these are science projects. They're production tools already used by real ML teams.

**Practical steps for a team to take this week:**

1. Add a validation check between "data received" and "data live." Even a simple label-consistency check, like the one demonstrated in the companion notebook, catches this class of attack before it ever reaches production.
2. Version training data like source code, so any update can be reviewed, audited, or rolled back.
3. Stop relying on overall accuracy as the only signal. Add monitoring that looks for small, targeted shifts in specific classes, not just the aggregate number.

**Who should be in the room for this:**

- **Data Science / ML Engineering** owns the model and the training pipeline. They're the ones who'd actually wire in a tool like Cleanlab or DVC.
- **Security Engineering** treats the training data pipeline as an attack surface, the same way they'd treat a code repository or an API.
- **Compliance and GRC** makes sure any customer or vendor supplied training data has a documented chain of custody, especially if that data includes anything that looks like personal information.
- **Product or business owners** decide how much risk is acceptable for a model that touches real transactions, since the fix is a process change, not just a technical one.

## Companion Notebook

`case_study_04_knn_poisoning.ipynb` is a runnable notebook that demonstrates both attacks and the defense described above, live, with real output rather than a mockup. Built on the same KNN digit classifier from my AI/ML studies.
