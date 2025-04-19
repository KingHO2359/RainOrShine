<template>
  <div class="mb-6 p-4 bg-red-100 border-l-4 border-red-500 text-red-700">
    <p>{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{ error: string }>()
</script>
