import os
import time

def save_screenshot(driver, name_prefix='screenshot'):
    reports_dir = os.path.join(os.getcwd(), 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    timestr = time.strftime('%Y%m%d_%H%M%S')
    path = os.path.join(reports_dir, f"{name_prefix}_{timestr}.png")
    driver.save_screenshot(path)
    return path
