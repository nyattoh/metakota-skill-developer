# Context Engineering Notes (Skills)

## スラッシュコマンドとの差
- スラッシュコマンドは固定プロンプトをメイン文脈に追加する仕組み。
- Skillsは「いつ・何を・どの量で読むか」を設計する仕組み。
- 差はUIではなくコンテキスト構造にある。

## 段階的ロード
- 読み込み順: metadata -> SKILL.md -> agents(タスク仕様) -> references/scripts
- agentsはタスク実行直前に一括ロードされるため軽く保つ。

## Taskの捉え方
- Taskは一時的なワーカー（独立した文脈を持つ）。
- メインは判断と指揮、重い作業はTaskへ委譲する。
- 結果だけがメインに返るため文脈崩壊を防げる。

## agentsは仕様書
- agents/*.md は人格定義ではなく「役割・入力・出力・制約」を書く。
- 知識やテンプレは references に逃がす。

## referencesは教科書棚
- 1ファイル1トピックで分割する。
- 「いつ読むか」をタスク仕様に明記する。

## scriptsの役割
- 機械的・決定的作業は scripts に移す。
- LLMは判断、scriptsは実行。

## 再利用可能なコンポーネント
- 固定構造（SKILL.md/agents/references/scripts）が再利用性を担保する。
- クライアントが変わっても同じSkillを叩ける設計が理想。
