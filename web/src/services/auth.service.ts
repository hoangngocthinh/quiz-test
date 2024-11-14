import apiClient from "@/services/api.services";
import { ILogin, IUserRegister } from "@/types/auth";

const authService = {
	async login(params: ILogin): Promise<boolean> {
		const response = await apiClient.post('auth/token/', params);
		if (response.data) {
			localStorage.setItem('access', response.data.access);
			localStorage.setItem('refresh', response.data.refresh);
			return true
		}
		return false
	},

	logout() {
		localStorage.setItem('access', '')
		localStorage.setItem('refresh', '')
	},

	async register(params: IUserRegister) {
		const response = await apiClient.post('auth/registration/', params);
		return response
	}
}

export default authService;