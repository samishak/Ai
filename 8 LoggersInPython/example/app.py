import logging

# ==============================
# Logging configuration
# ==============================
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

# Create named logger
logger = logging.getLogger("ArithmeticApp")
logger.setLevel(logging.DEBUG)   # 🔥 THIS WAS MISSING

# ==============================
# Arithmetic functions
# ==============================
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} x {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error", exc_info=True)
        return None

# ==============================
# Function calls
# ==============================
add(10, 15)
sub(10, 5)
multiply(2, 2)
divide(10, 2)
divide(10, 0)
