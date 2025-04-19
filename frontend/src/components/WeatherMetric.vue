<template>
  <div class="p-3 bg-gray-50 rounded-lg text-center">
    <p class="text-sm text-gray-500">{{ label }}</p>
    <p class="font-semibold">{{ value }}</p>
    <p v-if="note" class="text-xs text-gray-500">{{ note }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string
  value: string
  note?: string
}>()
</script>
