import argparse
import json

from scraper.g2_scraper import scrape_g2
from scraper.capterra_scraper import scrape_capterra
from scraper.trustradius_scraper import scrape_trustradius


def main():
    parser = argparse.ArgumentParser(description="Pulsegen Review Scraper")

    parser.add_argument(
        "--company",
        required=True,
        help="Company name (example: Zoho, Freshworks)"
    )

    parser.add_argument(
        "--source",
        required=True,
        choices=["g2", "capterra", "trustradius"],
        help="Review source: g2 / capterra / trustradius"
    )

    parser.add_argument(
        "--start",
        required=True,
        help="Start date (YYYY-MM-DD)"
    )

    parser.add_argument(
        "--end",
        required=True,
        help="End date (YYYY-MM-DD)"
    )

    args = parser.parse_args()

    # Call appropriate scraper
    if args.source == "g2":
        reviews = scrape_g2(args.company, args.start, args.end)

    elif args.source == "capterra":
        reviews = scrape_capterra(args.company, args.start, args.end)

    else:  # trustradius
        reviews = scrape_trustradius(args.company, args.start, args.end)

    # Save output to JSON
    with open("output/reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)

    print(f"✅ {len(reviews)} reviews saved to output/reviews.json")


if __name__ == "__main__":
    main()
