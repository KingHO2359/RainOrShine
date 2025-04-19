<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useWeatherStore } from '@/stores/weather'

import WeatherSearchForm from '@/components/WeatherSearchForm.vue'
import WeatherCard from '@/components/WeatherCard.vue'
import WeatherError from '@/components/WeatherError.vue'
import WeatherEmptyState from '@/components/WeatherEmptyState.vue'

const store = useWeatherStore()
const { searchQuery, weatherData, loading, error } = storeToRefs(store)
const { searchWeather } = store
</script>
<template>
  <div class="min-h-screen bg-gradient-to-br from-sky-100 to-blue-50 p-4 md:p-8">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-3xl font-bold text-center mb-8 text-blue-800">Weather Forecast</h1>

      <WeatherSearchForm v-model="searchQuery" :loading="loading" @search="searchWeather" />

      <WeatherError v-if="error" :error="error" />
      <WeatherCard v-if="weatherData" :weatherData="weatherData" />
      <WeatherEmptyState v-if="!weatherData && !loading && !error">
        <p class="text-lg">Enter a location to see the weather forecast</p>
      </WeatherEmptyState>
    </div>
  </div>
</template>
