<template>
       <v-layout>
            <drawer-demo> </drawer-demo>
        <toolbar-demo></toolbar-demo>
        <content-demo></content-demo>
        <footer-demo></footer-demo>
       </v-layout>
</template>


<script>
import DrawerDemo from "@/components/demo/DrawerDemo";
import ToolbarDemo from "@/components/demo/ToolbarDemo";
import FooterDemo from "@/components/demo/FooterDemo";
import ContentDemo from "@/components/demo/ContentDemo";
export default {
    components: {
        DrawerDemo,
        ToolbarDemo,
        FooterDemo,
        ContentDemo
    }
}
</script>
