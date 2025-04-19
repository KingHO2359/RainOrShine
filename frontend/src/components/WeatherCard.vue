<template>
  <div class="bg-white rounded-xl shadow-lg overflow-hidden">
    <div class="bg-blue-600 text-white p-4 flex justify-between">
      <div>
        <h2 class="text-2xl font-bold">{{ weatherData.location.name }}</h2>
        <p>{{ weatherData.location.country }}</p>
      </div>
      <div class="text-right text-sm">
        <p>{{ weatherData.location.localtime }}</p>
        <p>{{ weatherData.location.region }}</p>
      </div>
    </div>

    <div class="p-6">
      <div class="flex flex-col md:flex-row items-center mb-6">
        <div class="flex items-center mb-4 md:mb-0 md:mr-6">
          <img :src="weatherData.current.condition.icon" class="w-16 h-16" />
          <div class="ml-4">
            <h3 class="text-4xl font-bold">{{ weatherData.current.temp_c }}°C</h3>
            <p class="text-gray-600">{{ weatherData.current.condition.text }}</p>
          </div>
        </div>
        <div class="flex-1 grid grid-cols-2 gap-4">
          <WeatherMetric label="Feels Like" :value="`${weatherData.current.feelslike_c}°C`" />
          <WeatherMetric label="Humidity" :value="`${weatherData.current.humidity}%`" />
        </div>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <WeatherMetric
          label="Wind"
          :value="`${weatherData.current.wind_kph} km/h`"
          :note="weatherData.current.wind_dir"
        />
        <WeatherMetric label="Pressure" :value="`${weatherData.current.pressure_mb} mb`" />
        <WeatherMetric label="Visibility" :value="`${weatherData.current.vis_km} km`" />
        <WeatherMetric label="UV Index" :value="weatherData.current.uv.toString()" />
        <WeatherMetric label="Cloud Cover" :value="`${weatherData.current.cloud}%`" />
        <WeatherMetric label="Precipitation" :value="`${weatherData.current.precip_mm} mm`" />
        <WeatherMetric label="Heat Index" :value="`${weatherData.current.heatindex_c}°C`" />
        <WeatherMetric label="Dew Point" :value="`${weatherData.current.dewpoint_c}°C`" />
      </div>

      <div class="mt-6 text-sm text-gray-500 text-right">
        Last updated: {{ weatherData.current.last_updated }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import WeatherMetric from './WeatherMetric.vue'
import type { WeatherData } from '@/types/weather'

defineProps<{ weatherData: WeatherData }>()
</script>
