<template>
  <form @submit.prevent="$emit('search')" class="mb-6">
    <div class="flex flex-col md:flex-row gap-2">
      <input
        v-model="input"
        type="text"
        placeholder="Enter city name..."
        class="flex-1 px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
        :disabled="loading"
      />
      <button
        type="submit"
        class="px-6 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
        :disabled="loading"
      >
        <span v-if="loading">Searching...</span>
        <span v-else>Search</span>
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  modelValue: string
  loading: boolean
}>()

const emit = defineEmits(['update:modelValue', 'search'])

const input = ref(props.modelValue)

watch(
  () => props.modelValue,
  (val) => {
    input.value = val
  },
)

watch(input, (val) => {
  emit('update:modelValue', val)
})
</script>
