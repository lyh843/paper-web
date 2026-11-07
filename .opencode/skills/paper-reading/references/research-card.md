# Optional Research Card

A portable summary for a user who asks to compare, reproduce, cite, or build on a paper. The card format is optional; the default deep read's assumption, reproduction, counterexample, subsequent-literature search, and follow-up sections are mandatory under [research-extension](research-extension.md). The card supplements that same-HTML explanation and is never the sole final artifact. Include only fields relevant to the request.

```yaml
paper: {title, authors, source, version}
problem: ...
core_idea: ...
method_path: ...
key_mechanisms: [{operation, why_it_matters, source}]
experiment_links:
  - {question, setup, control, metric, result, source, interpretation}
findings: [{finding, scope, source, uncertainty}]
relation_to_user_work: {overlap, difference, reusable, potential_baseline}
reproduction_notes: {data, code, settings, missing_details}
next_questions: [{gap, hypothesis, minimal_test}]
```

Do not invent a `relation_to_user_work` when no research context was supplied. A recommended next action is useful only if the user asked for a decision. Every substantive paper fact should have a source pointer.
