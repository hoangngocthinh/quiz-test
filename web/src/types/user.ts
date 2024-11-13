export interface UserState {
  id: string | null;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  password?: string;
  password1?: string;
}
