<template>
	<section class="vh-100">
		<div class="container-fluid h-custom">
			<div class="row d-flex justify-content-center align-items-center h-100">
				<div class="col-md-9 col-lg-6 col-xl-5">
					<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
								class="img-fluid" alt="Sample image">
				</div>
				<div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
					<form class="mt-5" @submit.prevent="handleLogin">
							<!-- Email input -->
							<div class="form-outline mb-4">
									<input type="email" id="email" class="form-control form-control-lg" autocomplete="email"
											placeholder="Enter a valid email address" v-model="email" required/>
									<label class="form-label" for="email">Email address</label>
							</div>

							<!-- Password input -->
							<div class="form-outline mb-3">
									<input type="password" autocomplete="password"
											id="password" class="form-control form-control-lg"
											placeholder="Enter password" v-model="password" required/>
									<label class="form-label" for="password">Password</label>
							</div>

							<div class="d-flex justify-content-between align-items-center">
									<!-- Checkbox -->
									<div class="form-check mb-0">
											<input class="form-check-input me-2" type="checkbox" value="" id="form2Example3" />
											<label class="form-check-label" for="form2Example3">
													Remember me
											</label>
									</div>
									<a href="#!" class="text-body">Forgot password?</a>
							</div>
							<div class="text-center text-lg-start mt-4 pt-2">
									<button type="submit" class="btn btn-primary btn-lg"
											style="padding-left: 2.5rem; padding-right: 2.5rem;">Login</button>
									<p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <a href="#!"
													class="link-danger">
													| <router-link to="/register">Register</router-link>
											</a></p>
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
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { toast } from 'vue3-toastify';

export default defineComponent({
  setup() {
    const router = useRouter();
    const store = useStore();

    const email = ref('');
    const password = ref('');
    const errorMessage = ref<string | null>(null);

    const handleLogin = async () => {
      try {
        await store.dispatch('authModule/login', {
          email: email.value,
          password: password.value,
        });

        // Reset error message and redirect page
        errorMessage.value = null;
        toast("Login successful!", { autoClose: 1000 });
        router.push('/');
      } catch (error) {
        errorMessage.value = 'Login failed. Please check your credentials.';
      }
    };

    return {
      email,
      password,
      errorMessage,
      handleLogin,
    };
  },
});
</script>
