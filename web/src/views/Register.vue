<template>
<section class="vh-100">
		<div class="container-fluid h-custom">
			<div class="row d-flex justify-content-center align-items-center h-100">
				<div class="col-md-9 col-lg-6 col-xl-5">
					<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
								class="img-fluid" alt="Sample image">
				</div>
				<div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
					<form class="mt-5" @submit.prevent="register">
							<!-- Username input -->
							<div class="form-outline mb-3">
								<input type="text" id="username" class="form-control form-control-lg"
										placeholder="Enter Username" v-model="username" required/>
								<label class="form-label" for="username">Username</label>
							</div>
							<!-- First Name input -->
							<div class="form-outline mb-3">
								<input type="text" id="first_name" class="form-control form-control-lg"
										placeholder="Enter First Name" v-model="first_name" required/>
								<label class="form-label" for="first_name">First name</label>
							</div>
							<!-- Last Name input -->
							<div class="form-outline mb-3">
								<input type="text" id="last_name" class="form-control form-control-lg"
										placeholder="Enter Last Name" v-model="last_name" required/>
								<label class="form-label" for="last_name">Last name</label>
							</div>
							<!-- Email input -->
							<div class="form-outline mb-3">
								<input type="email" id="email" class="form-control form-control-lg"
										placeholder="Enter a valid email address" v-model="email" required/>
								<label class="form-label" for="email">Email address</label>
							</div>

							<!-- Password input -->
							<div class="form-outline mb-3">
								<input type="password"
										id="password" class="form-control form-control-lg"
										placeholder="Enter password" v-model="password" required/>
								<label class="form-label" for="password">Password</label>
							</div>
							<!-- Password input -->
							<div class="form-outline mb-3">
								<input type="password"
										id="password1" class="form-control form-control-lg"
										placeholder="Enter password verify" v-model="password1" required/>
								<label class="form-label" for="password1">Password Verify</label>
							</div>
							<div class="text-center text-lg-start mt-4 pt-2">
								<button type="submit" class="btn btn-primary btn-lg"
										style="padding-left: 2.5rem; padding-right: 2.5rem;">Register</button>
							</div>
					</form>
					<p v-if="errorMessage" class="error">{{ errorMessage }}</p>
				</div>
			</div>
		</div>
	</section>
</template>
  
<script lang="ts">
  import { defineComponent, ref } from 'vue';
	import axios from '../services/quiz.service';
	import { toast } from 'vue3-toastify';
	import { useRouter } from 'vue-router';
	const router = useRouter();

  
  export default defineComponent({
    setup() {
      const username = ref('');
      const first_name = ref('');
      const last_name = ref('');
      const email = ref('');
      const password = ref('');
      const password1 = ref('');
      const errorMessage = ref<string | null>(null);
  
      const register = async () => {
        try {
					if ( password.value != password1.value ) {
						errorMessage.value = 'Password not same.';
						return
					}
          const response = await axios.post('auth/registration/', {
            username: username.value,
            first_name: first_name.value,
            last_name: last_name.value,
            email: email.value,
            password: password.value,
						password1: password1.value,
          });

          errorMessage.value = null;
					toast("Registration successful! You can now log in!", {
						autoClose: 1000,
					}); // ToastOptions
					router.push('/login');
          console.log('Registration successful:', response.data);
        } catch (error) {
					toast("Registration failed. Please try again.!", {
						autoClose: 1000,
					});
          errorMessage.value = 'Registration failed. Please try again.';
        }
      };
  
      return {
        username,
        email,
        password,
				password1,
        first_name,
        last_name,
        errorMessage,
        register,
      };
    },
  });
  </script>
  
  <style scoped>
  .register-form {
    max-width: 400px;
    margin: auto;
  }
  .error {
    color: red;
  }
  .success {
    color: green;
  }
  </style>
  
