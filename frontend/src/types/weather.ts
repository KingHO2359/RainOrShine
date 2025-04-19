export interface WeatherCondition {
  text: string
  icon: string
  code: number
}

export interface CurrentWeather {
  temp_c: number
  feelslike_c: number
  humidity: number
  condition: WeatherCondition
  wind_kph: number
  wind_dir: string
  pressure_mb: number
  vis_km: number
  uv: number
  cloud: number
  precip_mm: number
  heatindex_c: number
  dewpoint_c: number
  last_updated: string
}

export interface Location {
  name: string
  country: string
  region: string
  localtime: string
}

export interface WeatherData {
  location: Location
  current: CurrentWeather
}
