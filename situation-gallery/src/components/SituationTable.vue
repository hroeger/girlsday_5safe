<!-- eslint-disable vue/no-deprecated-slot-attribute -->
<template>
  <div class="situation-table-wrapper">
    <scale-table>
      <table>
        <thead>
          <tr>
            <!-- <th>#</th> -->
            <th>Bewertung</th>
            <th>Situation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in selectedRatings" :key="index">
            <!-- <td class="id-cell">{{ index + 1 }}</td> -->
            <td class="rating-cell">
              <div style="flex: 9999; display: flex; flex-wrap: wrap" class="radio-group">
                <scale-radio-button
                  label="keine Gefahr"
                  :name="'standard' + index"
                  :input-id="'good' + index"
                  :checked="item.rating === false"
                  @scale-change="updateSelectedRatings(index, false)"
                ></scale-radio-button>
                <scale-radio-button
                  label="Gefahr"
                  :name="'standard' + index"
                  :input-id="'bad' + index"
                  :checked="item.rating"
                  @scale-change="updateSelectedRatings(index, true)"
                ></scale-radio-button>
              </div>
            </td>
            <td class="image-cell">
              <img
                :src="PATH_PREFIX + item.name"
                alt="Situation"
                style="width: 100%; height: 100%; object-fit: cover"
              />
            </td>
          </tr>
          <tr>
            <td></td>
            <td>
              <scale-button @click="handleSend">Senden</scale-button>
              <scale-button @click="reset">Reset</scale-button>
            </td>
          </tr>
        </tbody>
      </table>
    </scale-table>
  </div>
  <scale-notification
    v-show="errorMessage !== ''"
    class="notificationToast"
    type="toast"
    variant="danger"
    heading="Fehler"
    delay="3000"
    dismissible
    :opened="errorMessage !== ''"
    @scale-close="errorMessage = ''"
  >
    <span slot="text">{{ errorMessage }}</span>
  </scale-notification>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { Rating } from '../types/Rating'
import ApiService from '../service/service'
import router from '../router'

const PATH_PREFIX = '/src/assets/img/'

const images = import.meta.glob('/src/assets/img/*')
const selectedRatings = ref(generateRatingObjects(images))

const errorMessage = ref('')

const updateSelectedRatings = (id: number, rating: boolean) => {
  selectedRatings.value[id].rating = rating
}

const handleSend = async () => {
  try {
    const result = await ApiService.sendPostRequest(selectedRatings.value)
    if (result?.status === 200) {
      router.push({ name: 'success' })
    }
  } catch (error) {
    errorMessage.value = 'Fehler beim Senden des Protokolls'
  }
}

const reset = () => {
  selectedRatings.value = generateRatingObjects(images)
}

function generateRatingObjects(images: Record<string, () => Promise<unknown>>) {
  return Object.keys(images).map((item, index) =>
    reactive({
      id: index,
      name: item.replace(PATH_PREFIX, ''),
      rating: null
    } as Rating)
  )
}
</script>

<style scoped lang="scss">
.situation-table-wrapper {
  height: 100%;
  width: 100%;
  font-size: x-large;
  padding: 5rem 0;
  scale-table {
    --font-size: x-large;
    width: 100%;
    height: 100%;
    th {
      padding: 10px;
    }
    .id-cell {
      width: 2%;
    }
    .rating-cell {
      min-width: 465px;
      width: 33%;
    }
    .image-cell {
      width: 35%;
    }
  }
  .radio-group {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    scale-radio-button {
      margin-right: 40px;
    }
  }
  scale-button {
    margin: 1rem;
    float: right;
  }
}
.notificationToast::part(base) {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 99;
  max-width: 90%;
}
</style>
