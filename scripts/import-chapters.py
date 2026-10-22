# -*- coding: utf-8 -*-
"""Copy the thirteen SAD chapters into Quartz and drop course-admin pointers."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

SOURCE = Path(r"D:\E1\110 系統分析與設計\01-Course-Materials")
CONTENT = Path(r"D:\E1\sad-notes\content")
DEST = CONTENT / "教材"

CHAPTERS = [
    (
        "01-Systems-and-Analysis.md",
        "系統分析與設計導論",
        "分析",
        "系統與資訊系統的組成、分析與設計的分界、開發生命週期，以及系統為什麼會失敗。",
    ),
    (
        "02-Problem-Definition.md",
        "問題定義與現況分析",
        "分析",
        "從既有系統反推要解決的問題：5 Why、魚骨圖、可驗收的目標與問題定義。",
    ),
    (
        "03-User-Analysis.md",
        "使用者分析",
        "分析",
        "利害關係人、使用者分群、使用案例圖、流程分析與事件表。",
    ),
    (
        "04-System-Requirements-Analysis.md",
        "系統需求分析",
        "分析",
        "把使用案例展開成功能需求與非功能需求，並檢查需求品質與追溯。",
    ),
    (
        "05-Functional-Analysis.md",
        "功能分析",
        "分析",
        "系統邊界、情境圖、功能分解、模組劃分與 CRUD 矩陣。",
    ),
    (
        "06-Behavioral-Modeling.md",
        "行為建模",
        "分析",
        "活動圖與泳道、系統循序圖、狀態機圖，以及三張圖怎麼互相核對。",
    ),
    (
        "07-Data-Modeling.md",
        "資料建模與資料庫設計",
        "分析",
        "實體關聯圖、從需求找實體、正規化、資料字典與值域。",
    ),
    (
        "08-System-Architecture.md",
        "系統環境與架構",
        "設計",
        "使用者端、應用系統與資料庫的三段結構，以及系統放在哪裡、和誰連。",
    ),
    (
        "09-Feasibility-and-Risk.md",
        "可行性、限制與風險分析",
        "設計",
        "技術、經濟、組織、時程四種可行性，以及限制與風險如何回頭改設計。",
    ),
    (
        "10-Object-Modeling.md",
        "物件建模",
        "設計",
        "概念類別圖：類別、關係、多重性，以及它和實體關聯圖的差別。",
    ),
    (
        "11-System-Interface-and-Data-Exchange.md",
        "系統介面與資料交換設計",
        "設計",
        "兩套系統之間交換什麼、何時交換、失敗了怎麼處理。",
    ),
    (
        "12-UI-Design.md",
        "使用者介面設計",
        "設計",
        "從需求與流程推出畫面，並把畫面上的欄位對回資料字典。",
    ),
    (
        "13-Design-Specification.md",
        "系統設計規格與追溯",
        "設計",
        "把各章產出收成一套設計，用追溯鏈檢查它們講的是不是同一套系統。",
    ),
]

EXCLUDED_LINK = re.compile(
    r"\[([^\]]+)\]\(\.\./(?:"
    r"00-Course-Introduction|"
    r"02-Midterm-Project-Example-Reports|"
    r"03-Midterm-Project-Example-Systems|"
    r"04-Final-Project-Example-Reports|"
    r"05-Final-Project-Topics"
    r")/[^)]+\)"
)

MARKER = re.compile(r"\s*[🔴🔵]\s*(?:期中必讀|期末必讀)")


def drop_admin_blockquote(line: str) -> str | None:
    stripped = line.lstrip()
    if not stripped.startswith(">"):
        return line
    if "各項產出實際要怎麼做" in line:
        return "> **延伸閱讀**：本章不談任何具體的分析方法或圖表畫法。各項產出實際要怎麼做，見後續各章。\n"
    if "必讀標記" in line or "對應範例報告" in line:
        return None
    if "延伸閱讀" in line and any(
        token in line for token in ("報告內容", "範例報告說明", "Deliverables", "各組")
    ):
        return None
    return line


def transform(text: str) -> str:
    kept: list[str] = []
    for line in text.splitlines(keepends=True):
        updated = drop_admin_blockquote(line)
        if updated is None:
            continue
        kept.append(updated)
    text = "".join(kept)
    text = EXCLUDED_LINK.sub(r"\1", text)
    text = MARKER.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.lstrip("\n")


def frontmatter(title: str, tag: str, description: str, body: str) -> str:
    if body.startswith("---"):
        return body
    return (
        "---\n"
        f"title: {title}\n"
        "tags:\n"
        f"  - {tag}\n"
        f"description: {description}\n"
        "---\n\n"
        + body
    )


def copy_images() -> None:
    image_src = SOURCE / "images"
    image_dest = DEST / "images"
    if image_dest.exists():
        shutil.rmtree(image_dest)
    shutil.copytree(
        image_src,
        image_dest,
        ignore=shutil.ignore_patterns("*.puml"),
    )


def write_index() -> None:
    analysis = [item for item in CHAPTERS if item[2] == "分析"]
    design = [item for item in CHAPTERS if item[2] == "設計"]

    def items(rows: list[tuple[str, str, str, str]]) -> str:
        return "\n".join(
            f"- [{title}](教材/{filename})：{description}"
            for filename, title, _tag, description in rows
        )

    text = f"""---
title: 系統分析與設計
description: 從問題定義到設計規格的讀書筆記。
---

這是一套系統分析與設計的讀書筆記。正文整理自元智大學工業工程與管理學系呂卓勲的教材，原倉庫為 [system-analysis-and-design](https://github.com/billy1125/system-analysis-and-design)，授權為 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hant)。

閱讀順序是先把一套系統看懂，再把它設計出來。

## 分析

先弄清問題、人與需求，再把功能、行為和資料畫出來。

{items(analysis)}

## 設計

決定系統放在哪裡、記得住什麼、畫面長什麼樣，並檢查這些文件講的是不是同一套系統。

{items(design)}
"""
    (CONTENT / "index.md").write_text(text, encoding="utf-8")


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    for filename, title, tag, description in CHAPTERS:
        raw = (SOURCE / filename).read_text(encoding="utf-8")
        body = frontmatter(title, tag, description, transform(raw))
        (DEST / filename).write_text(body, encoding="utf-8")
    copy_images()
    write_index()
    print(f"wrote {len(CHAPTERS)} chapters and index")


if __name__ == "__main__":
    main()
