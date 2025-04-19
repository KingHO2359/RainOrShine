import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { WeatherData } from '@/types/weather'

export const useWeatherStore = defineStore('weather', () => {
  const searchQuery = ref('')
  const weatherData = ref<WeatherData | null>(null)
  const loading = ref(false)
  const error = ref('')

  const searchWeather = async () => {
    if (!searchQuery.value.trim()) {
      error.value = 'Please enter a location'
      return
    }

    loading.value = true
    error.value = ''
    weatherData.value = null

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/weather/?location=${encodeURIComponent(searchQuery.value)}`,
      )

      if (!response.ok) throw new Error(`HTTP ${response.status}`)

      const data = await response.json()
      weatherData.value = data as WeatherData
    } catch (err) {
      console.error(err)
      error.value = 'Failed to fetch weather data.'
    } finally {
      loading.value = false
    }
  }

  return {
    searchQuery,
    weatherData,
    loading,
    error,
    searchWeather,
  }
})
