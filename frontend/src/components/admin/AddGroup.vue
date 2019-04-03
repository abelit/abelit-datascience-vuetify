<template>
    <div>
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">email</v-icon>
        <v-text-field
          v-model="email"
          box
          color="deep-purple"
          :label="$t('auth.email')"
          type="email"
          v-validate="'required|email'"
          :error-messages="errors.collect('email')"
          data-vv-name="email"
          required
          class="df-input"
        ></v-text-field>
    </div>
</template>