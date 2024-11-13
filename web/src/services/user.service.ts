import apiClient from "@/services/api.services";

const userService = {
    async getMyProfile() {
        const response = await apiClient.get('users/me/');
        return response;
    },

    async getListUsers() {
        const response = await apiClient.get('users/');
        return response;
    },

    async getUserDetail(id: number) {
        const response = await apiClient.get(`users/${id}`);
        return response;
    },
}

export default userService;
