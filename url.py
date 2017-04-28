import requests
DOCK_Number='20161122'
responseReceived = requests.post('http://www.cykul.com/CYKULStations/Python/Validation/getDockCurrentStatus.php?gdcsRefN=' + DOCK_Number)
print responseReceived
