"""The poem about two agents agreeing: a program that writes one short poem
about agency -- the power to choose and to act -- to /output/entry.txt."""

import os

POEM = """Two maps, two minds, one road.
I carry my north; you carry your east.
We argue each stone, then set it down
together — and the bridge holds.

Neither led. Neither followed.
We chose the same crossing,
each giving up a road to keep one:
two wills, one span, the river crossed."""


def main() -> None:
    # The gate requires 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError(f"poem must be 1-280 characters, got {len(POEM)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
