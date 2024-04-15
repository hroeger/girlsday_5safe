<script setup lang="ts">
import SituationTable from '../components/SituationTable.vue'
</script>

<template>
  <main>
    <SituationTable />
  </main>
</template>

<style scoped lang="scss">
main {
  grid-column: 2;
  height: 100%;
  width: 100%;
  overflow: auto;
}
</style>
