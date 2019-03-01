<template>
  <div class="about">
    <h1>This is an about page</h1>
    <input v-validate="'required'" name="myinput"  class="form-control" type="text">
<span>{{ errors.first('myinput') }}</span>
  </div>
</template>

<style media="screen">
  
</style>
