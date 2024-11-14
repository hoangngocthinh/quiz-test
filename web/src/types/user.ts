export interface IUser {
  id: string | null;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  password?: string;
  password1?: string;
}

export interface UserState {
  user: IUser
}
