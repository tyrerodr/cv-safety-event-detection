from pathlib import Path
import json
from typing import Any
from video_writer import generate_visualization_video


DEFAULT_ANNOTATIONS_PATH = Path("data/sample_annotations.json")
DEFAULT_OUTPUT_VIDEO_PATH = Path("outputs/output.mp4")


def load_annotations(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Annotations file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    annotations = load_annotations(DEFAULT_ANNOTATIONS_PATH)

    print(f"Loaded {len(annotations)} frames")

    events = generate_visualization_video(
        annotations=annotations,
        output_path=DEFAULT_OUTPUT_VIDEO_PATH,
    )

    print(f"Total events detected: {len(events)}")
    print(f"Video saved to: {DEFAULT_OUTPUT_VIDEO_PATH}")


if __name__ == "__main__":
    main()