<template>
    <div>
      <h2>Create Quiz Session</h2>
      <form @submit.prevent="createSession">
        <input v-model="quizId" placeholder="Quiz ID" />
        <input v-model="startTime" placeholder="Start Time" />
        <input v-model="endTime" placeholder="End Time" />
        <input v-model="maxParticipants" type="number" placeholder="Max Participants" />
        <button type="submit">Create Session</button>
      </form>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import axios from '../services/quiz.service';
  
  export default defineComponent({
    setup() {
      const quizId = ref('');
      const startTime = ref('');
      const endTime = ref('');
      const maxParticipants = ref<number | null>(null);
  
      const createSession = async () => {
        try {
          const response = await axios.post('quiz-session/create/', {
            quiz: quizId.value,
            start_time: startTime.value,
            end_time: endTime.value,
            max_participants: maxParticipants.value,
          });
          console.log('Session created:', response.data);
        } catch (error) {
          console.error('Error creating session:', error);
        }
      };
  
      return {
        quizId,
        startTime,
        endTime,
        maxParticipants,
        createSession,
      };
    },
  });
  </script>
  
  <style scoped>
  /* CSS cho component */
  </style>
  