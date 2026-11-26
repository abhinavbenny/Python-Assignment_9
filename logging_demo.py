
import logging

# Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


def process_order(price, discount_percent):
    logger.debug("Starting order processing")

    try:
        if price < 0:
            raise ValueError("Price cannot be negative")

        if not 0 <= discount_percent <= 100:
            raise ValueError("Invalid discount percentage")

        logger.info("Order received successfully")

        discount = price * discount_percent / 100
        discounted_price = price - discount

        logger.debug("Discount calculated: %.2f", discount)

        gst = discounted_price * 0.18
        total = discounted_price + gst

        logger.info("GST calculated: %.2f", gst)
        logger.info("Final order total: %.2f", total)

        return round(total, 2)

    except ValueError as error:
        logger.error("Order processing failed: %s", error)
        return None


if __name__ == "__main__":
    logger.info("Application started")

    process_order(1000, 10)
    process_order(-500, 10)
    process_order(2000, 120)

    logger.warning("Application demonstration completed")

    print("Order processing completed.")
    print("Check application.log for logging details.")
