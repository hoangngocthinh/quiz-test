export interface AuthState {
  isAuthenticated: boolean
}

export interface ILogin {
  email: string
  password: string
}

export interface IUserRegister extends ILogin {
  username: string
  password1: string
  first_name: string
  last_name: string
}