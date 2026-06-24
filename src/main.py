from pathlib import Path
import json
from typing import Any
from geometry import enrich_detection_with_position


DEFAULT_ANNOTATIONS_PATH = Path("data/sample_annotations.json")


def load_annotations(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Annotations file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    annotations = load_annotations(DEFAULT_ANNOTATIONS_PATH)

    print(f"Loaded {len(annotations)} frames")

    for frame in annotations:
        frame_num = frame["Frame_num"]
        timestamp = frame["Timestamp"]
        frame_width = frame["Frame_width"]
        frame_height = frame["Frame_height"]
        
        # The same as the commented code below, but using a list comprehension instead of a for loop
        # enriched_detections = []

        # for detection in frame["detections"]:
        #     enriched_detection = enrich_detection_with_position(
        #         detection=detection,
        #         frame_width=frame_width,
        #         frame_height=frame_height,
        #     )
        #     enriched_detections.append(enriched_detection)

        enriched_detections = [
            enrich_detection_with_position(
                detection=detection,
                frame_width=frame_width,
                frame_height=frame_height,
            )
            for detection in frame["detections"]
        ]

        print(f"\nFrame {frame_num} | Timestamp: {timestamp}")

        for detection in enriched_detections:
            print(
                f"- {detection['class']} "
                f"id={detection['object_id']} "
                f"bbox_pixels={detection['bbox_pixels']} "
                f"point={detection['point']}"
            )


if __name__ == "__main__":
    main()