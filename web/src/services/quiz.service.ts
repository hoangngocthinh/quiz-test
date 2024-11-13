import apiClient from "@/services/api.services";

const quizService = {
    async getQuizes(params: any) {
        return await apiClient.get('quiz/', {params: params});
    },
}

export default quizService;