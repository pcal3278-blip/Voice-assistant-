from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class CastBlock:
    """Represents one CAST segment (e.g., Block 1, Block 2)."""

    name: str
    items: List[str] = field(default_factory=list)

    def add_item(self, text: str) -> None:
        cleaned = text.strip()
        if not cleaned:
            raise ValueError(f"Cannot add empty text to {self.name}")
        self.items.append(cleaned)

    def render(self) -> str:
        lines = [f"## {self.name}"]
        for index, item in enumerate(self.items, start=1):
            lines.append(f"{index}. {item}")
        return "\n".join(lines)


class CAST25ScriptManager:
    """Builds, organizes, and exports a CAST25-ready script for TTS workflows."""

    DEFAULT_BLOCKS = [
        "Block 1 - Open and Top Story",
        "Block 2 - National and World",
        "Block 3 - Business and Tech",
        "Block 4 - Local and Weather",
        "Block 5 - Close",
    ]

    SUPPORTED_VOICES = {"bella", "mac"}

    def __init__(self, blocks: Optional[List[str]] = None, voice: str = "bella") -> None:
        block_names = blocks or self.DEFAULT_BLOCKS
        if not block_names:
            raise ValueError("At least one CAST block is required")

        self.blocks: Dict[str, CastBlock] = {name: CastBlock(name=name) for name in block_names}
        self.voice = self._validate_voice(voice)

    def _validate_voice(self, voice: str) -> str:
        normalized = voice.strip().lower()
        if normalized not in self.SUPPORTED_VOICES:
            supported = ", ".join(sorted(self.SUPPORTED_VOICES))
            raise ValueError(f"Unsupported voice '{voice}'. Use one of: {supported}")
        return normalized

    def set_voice(self, voice: str) -> None:
        self.voice = self._validate_voice(voice)

    def add_verified_news(self, block_name: str, text: str, source: Optional[str] = None) -> None:
        if block_name not in self.blocks:
            raise ValueError(f"Unknown block '{block_name}'")

        source_prefix = f"[Source: {source}] " if source else ""
        self.blocks[block_name].add_item(f"{source_prefix}{text}")

    def load_verified_lines(self, block_name: str, lines: List[str], source: Optional[str] = None) -> None:
        for line in lines:
            self.add_verified_news(block_name=block_name, text=line, source=source)

    def render_script(self) -> str:
        header = [
            "CAST25 Script",
            f"Voice: {self.voice}",
            "",
        ]
        body = [block.render() for block in self.blocks.values()]
        return "\n\n".join(header + body)

    def export_script(self, output_path: str | Path) -> Path:
        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(self.render_script(), encoding="utf-8")
        return destination
