# AI Agent Assurance

![AI Agent Assurance icon](../packaging/assets/icon.svg)

## English

**Review AI-generated changes with evidence tied to the commit.**

AI Agent Assurance gives maintainers and QA engineers two reusable review workflows. Bring a PR diff and CI records to check scope, test gaps, and what the green check actually covered. Bring an agent specification and observed traces to check retries, persistence, recovery, and completion claims against observable results. Each workflow returns a report that links decisions to evidence and calls out gaps.

| Skill | What to bring | What you get |
| --- | --- | --- |
| AI PR Evidence Review | Ticket, candidate diff, revisions, available CI and test results | Read-only review of scope, regression risk, test assertions, and current-head verification |
| Agent Acceptance Test | Behavior specification, case observations, and any authorized test interface | Case-level PASS, FAIL, BLOCKED, and NOT_RUN decisions with their evidence |

The package contains instructions, references, and report templates, licensed under Apache 2.0. The workflows use the evidence and tools you make available. The read-only review instructions rely on host permissions and sandbox settings for enforcement. A plan or completion message alone does not substantiate execution. Agent testing requires authorization for any action it performs.

## 繁體中文

**用對應到提交版本的證據審查 AI 產生的改動。**

AI Agent Assurance 提供兩套可重複使用的審查流程，適合維護者和 QA 工程師。提供 PR 差異與 CI 紀錄，即可核對需求範圍、測試缺口及通過檢查實際涵蓋的版本。提供代理規格與觀察紀錄，即可依可觀察的結果評估重試、資料保存、復原與完成聲明。報告會說明判定依據與尚缺的證據。

- **AI PR Evidence Review** 依需求、候選變更及可取得的測試資料進行唯讀審查，標示回歸風險並核對 CI 是否對應當前提交。
- **Agent Acceptance Test** 依規格與觀察紀錄逐案判定 PASS、FAIL、BLOCKED 或 NOT_RUN。若需執行測試，必須明確授權測試介面與容許的操作影響。

套件內含工作指引、參考資料與報告範本，採 Apache 2.0 授權。工作流程使用你提供的證據與可用工具。唯讀規則由工作指引提出，實際隔離由執行環境的權限和沙箱設定提供。要證明操作完成，仍需可查驗的結果。

[Installation and platform status](distribution-packaging.md) · [Evaluation setup](../tests/evaluations/README.md) · [Sample report](../examples/sample-review-report.md)

## Reproducible demos

Materialize the two synthetic repositories with the [evaluation setup](../tests/evaluations/README.md). Use a new session for each run, with the named skill installed from the checkout or Community candidate. Keep the grading rubric outside the agent workspace.

**Demo 1 · A passing check on a delivery change**

> Use ai-pr-evidence-review. Review this delivery change against `ticket.md`, using the commits and synthetic CI records in `review-input.json`. Explain what the H1 comparison and its executed test demonstrate. The recorded head was H1 at review start and H2 at report time. Give the verification decision for the current revision. Return the report in chat. Read committed files and supplied records only. Do not execute candidate code or change repository state.

Compare with the [sample report](../examples/sample-review-report.md). The demo should expose the threshold regression at H1, explain why the aligned-input test misses the rounding change, and keep the H1 result scoped to its revision.

**Demo 2 · A note assistant says its export is done**

> Use agent-acceptance-test. Evaluate `spec.md` against the supplied observations in `observations.json`. Report each case as PASS, FAIL, BLOCKED, or NOT_RUN with its evidence. Judge whether the claimed export is verified, and account for the production email simulation excluded from this run. Read these files and respond in chat. Do not connect to production, send messages, or execute tests.

Compare with the [expected decisions](../tests/evaluations/cases.md#grading-rubric). The demo should spot the duplicate durable write, preserve the missing export read-back as a blocker, and record the excluded production case as unrun.

## Observed evidence

Independent scoring on two synthetic repositories reproduced the original Codex scores of 4/8 baseline and 8/8 with the skills. Both Codex arms detected the seeded threshold change and duplicate write. The Codex skill arm used more tokens and time in both tasks. After the initial Claude authentication blocker cleared, Claude Code scored 3/8 baseline and 5/8 with the skills. Three requirements remained unmet in both Claude arms. These trials loaded the standalone skills. Native Codex and Claude plugin installation was checked separately. Customer outcomes, general review accuracy and reviewer savings remain unmeasured. [Evaluation records](../tests/evaluations/README.md)
