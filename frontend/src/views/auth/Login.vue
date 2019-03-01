<template>
 <div class="login-container container-fluid">
    <v-card
    class="mx-auto"
    style="max-width: 500px; margin-top:15%;"
    color="#eaeaeaa1"
  >
    <v-toolbar
      color="#01074ccf !important"
      cards
      dark
      flat
    >
    <v-icon size=36 color="#efefef">account_box</v-icon>
      <v-card-title class="title font-weight-regular" style="margin: 0 auto;">{{$t('m.loginPage')}}</v-card-title>
   
    </v-toolbar>
    <v-form
      ref="form"
      v-model="form"
      class="pa-3 pt-4"
    >
    <v-icon size=36 color="#efefef" style="float: left;" class="df-icon">person</v-icon>
      <v-text-field
        v-model="name"
        box
        color="deep-purple"
        :label="$t('m.email')+'/'+$t('m.name') "
        type="name"
        v-validate="'required'"
        :error-messages="errors.collect('name')"
        data-vv-name="name"
        required
        class="df-input"
      ></v-text-field>

      <v-icon size=36 color="#efefef" style="float: left;" class="df-icon">lock</v-icon>
      <v-text-field
        v-model="password"
        box
        color="deep-purple"
        counter="18"
        :label="$t('m.password')"
        style="min-height: 96px; "
        :append-icon="showPassword ? 'visibility_off' : 'visibility'"
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
        v-validate="'required|max:18|min:8'"
        :error-messages="errors.collect('password')"
        data-vv-name="password"
        required
      ></v-text-field>
    </v-form>
    <v-divider></v-divider>
    
    <v-card-actions>
       <v-btn
        flat
        class="title font-weight-regular"
      >
        <router-link to="/register">{{$t('m.register')}}?</router-link>
      </v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!form"
        :loading="isLoading"
        class="white--text title font-weight-regular"
        color="#01074ccf"
        depressed
      >{{$t('m.login')}}</v-btn>
    </v-card-actions>
  </v-card>
 </div>
</template>

<script>
  export default {
    data: () => ({
      showPassword: false,
      email: undefined,
      form: false,
      isLoading: false,
      password: undefined,
    })
  }
</script>

<style lang="css">
  .login-container {
    width: 100%;
    height: 100%;
    background-image:  url('../../assets/login/login5.jpg');
    background-repeat:no-repeat; 
    background-size:100% 100%;
    -moz-background-size:100% 100%;
    /* background-color: #ff7700;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 900'%3E%3Cpolygon fill='%23cc0000' points='957 450 539 900 1396 900'/%3E%3Cpolygon fill='%23aa0000' points='957 450 872.9 900 1396 900'/%3E%3Cpolygon fill='%23d6002b' points='-60 900 398 662 816 900'/%3E%3Cpolygon fill='%23b10022' points='337 900 398 662 816 900'/%3E%3Cpolygon fill='%23d9004b' points='1203 546 1552 900 876 900'/%3E%3Cpolygon fill='%23b2003d' points='1203 546 1552 900 1162 900'/%3E%3Cpolygon fill='%23d3006c' points='641 695 886 900 367 900'/%3E%3Cpolygon fill='%23ac0057' points='587 900 641 695 886 900'/%3E%3Cpolygon fill='%23c4008c' points='1710 900 1401 632 1096 900'/%3E%3Cpolygon fill='%239e0071' points='1710 900 1401 632 1365 900'/%3E%3Cpolygon fill='%23aa00aa' points='1210 900 971 687 725 900'/%3E%3Cpolygon fill='%23880088' points='943 900 1210 900 971 687'/%3E%3C/svg%3E");
    background-attachment: fixed;
    background-size: cover; */
  }
  /* @media only screen and (max-width: 375px) {
            .login-container { 
              background-image:  url('../assets/login/login1.jpg');; 
            }
        } */

  .df-icon {
    position: relative;
    padding: 10px;
    background: #01074ccf;
    min-width: 50px;
    text-align: center;
  }
  .df-input {
    padding:10px;
  }
</style>