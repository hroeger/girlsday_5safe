import axios from 'axios'
import { Rating } from '../types/Rating'

export default {
  async sendPostRequest(data: Rating[]) {
    return await axios.post('http://127.0.0.1:5000', data)
  }
}
