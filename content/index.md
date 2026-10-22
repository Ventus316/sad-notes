---
title: 系統分析與設計
description: 從問題定義到設計規格的讀書筆記。
---

這是一套系統分析與設計的讀書筆記。正文整理自元智大學工業工程與管理學系呂卓勲的教材，原倉庫為 [system-analysis-and-design](https://github.com/billy1125/system-analysis-and-design)，授權為 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hant)。

閱讀順序是先把一套系統看懂，再把它設計出來。

## 分析

先弄清問題、人與需求，再把功能、行為和資料畫出來。

- [系統分析與設計導論](教材/01-Systems-and-Analysis.md)：系統與資訊系統的組成、分析與設計的分界、開發生命週期，以及系統為什麼會失敗。
- [問題定義與現況分析](教材/02-Problem-Definition.md)：從既有系統反推要解決的問題：5 Why、魚骨圖、可驗收的目標與問題定義。
- [使用者分析](教材/03-User-Analysis.md)：利害關係人、使用者分群、使用案例圖、流程分析與事件表。
- [系統需求分析](教材/04-System-Requirements-Analysis.md)：把使用案例展開成功能需求與非功能需求，並檢查需求品質與追溯。
- [功能分析](教材/05-Functional-Analysis.md)：系統邊界、情境圖、功能分解、模組劃分與 CRUD 矩陣。
- [行為建模](教材/06-Behavioral-Modeling.md)：活動圖與泳道、系統循序圖、狀態機圖，以及三張圖怎麼互相核對。
- [資料建模與資料庫設計](教材/07-Data-Modeling.md)：實體關聯圖、從需求找實體、正規化、資料字典與值域。

## 設計

決定系統放在哪裡、記得住什麼、畫面長什麼樣，並檢查這些文件講的是不是同一套系統。

- [系統環境與架構](教材/08-System-Architecture.md)：使用者端、應用系統與資料庫的三段結構，以及系統放在哪裡、和誰連。
- [可行性、限制與風險分析](教材/09-Feasibility-and-Risk.md)：技術、經濟、組織、時程四種可行性，以及限制與風險如何回頭改設計。
- [物件建模](教材/10-Object-Modeling.md)：概念類別圖：類別、關係、多重性，以及它和實體關聯圖的差別。
- [系統介面與資料交換設計](教材/11-System-Interface-and-Data-Exchange.md)：兩套系統之間交換什麼、何時交換、失敗了怎麼處理。
- [使用者介面設計](教材/12-UI-Design.md)：從需求與流程推出畫面，並把畫面上的欄位對回資料字典。
- [系統設計規格與追溯](教材/13-Design-Specification.md)：把各章產出收成一套設計，用追溯鏈檢查它們講的是不是同一套系統。
