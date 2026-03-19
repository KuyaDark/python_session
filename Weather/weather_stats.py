import pandas as pd

# Load your CSV file
df = pd.read_csv('no_rain.csv')

# Parse datetime column
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values('datetime').reset_index(drop=True)

# ── Update these to match your actual CSV column names ──────────────────
column_map = {
    'Pressure':          'sealevelpressure',
    'Temp':              'temp',
    'Relative Humidity': 'humidity',
    'Wind Speed':        'windspeed',
}
# ────────────────────────────────────────────────────────────────────────

# Convert Temperature: Fahrenheit → Celsius
df[column_map['Temp']] = (df[column_map['Temp']] - 32) * 5 / 9

# Convert Wind Speed: mph → m/s
df[column_map['Wind Speed']] = df[column_map['Wind Speed']] * 0.44704

# 1-hour trend = difference from 4 rows ago (4 x 15min = 1 hour)
PERIODS = 4

df['pressure_trend_1h'] = df[column_map['Pressure']].diff(periods=PERIODS)
df['temp_trend_1h']     = df[column_map['Temp']].diff(periods=PERIODS)
df['rh_trend_1h']       = df[column_map['Relative Humidity']].diff(periods=PERIODS)

# Build results
metrics = {
    'Pressure':             df[column_map['Pressure']],
    'Temp (°C)':            df[column_map['Temp']],
    'Relative Humidity':    df[column_map['Relative Humidity']],
    'Wind Speed (m/s)':     df[column_map['Wind Speed']],
    'Pressure Trends (1h)': df['pressure_trend_1h'],
    'Temp Trends (1h)':     df['temp_trend_1h'],
    'RH Trends (1h)':       df['rh_trend_1h'],
}

# Display min/max table
print(f"{'Metric':<25} {'Minimum':>12} {'Maximum':>12}")
print("-" * 50)
for label, series in metrics.items():
    print(f"{label:<25} {series.min():>12.2f} {series.max():>12.2f}")

# Export to CSV
results_df = pd.DataFrame({
    label: {'Minimum': series.min(), 'Maximum': series.max()}
    for label, series in metrics.items()
}).T

results_df.to_csv('weather_min_max.csv')
print("\nResults saved to weather_min_max.csv")