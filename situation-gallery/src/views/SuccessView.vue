<template>
  <div class="success-wrapper">
    <scale-card>
      <div class="content">
        <scale-icon-action-success accessibility-title="success" color="#008653" />
        <p>Das Protokoll wurde erfolgreich gesendet!</p>
        <scale-button size="small" @click="back">Zurück</scale-button>
      </div>
    </scale-card>
  </div>
</template>

<script setup lang="ts">
import router from '../router'

const back = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped lang="scss">
.success-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  flex: 1;
  justify-content: center;
  align-items: center;
  grid-column: 2;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}
</style>
