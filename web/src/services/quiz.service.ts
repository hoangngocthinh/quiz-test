import apiClient from "@/services/api.services";
import { SearchQuiz, SearchQuestion, Question } from "@/types/quiz";

const quizService = {
	async getQuizes(params: SearchQuiz) {
		return await apiClient.get('quiz', {params: params});
	},

	async getQuestions(params: SearchQuestion): Promise<Question> {
		return await apiClient.get('quiz/question', {params: params});
	},
	

	
}

export default quizService;