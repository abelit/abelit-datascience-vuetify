<template>
    <div>
        <h1>Slot子组件</h1>
        <div class="container">
        <header>
            <slot name="header">子组件内容：header插槽中原有的内容</slot>
        </header>
        <main>
            <slot>子组件内容：main插槽中原有的内容</slot>
        </main>
        <footer>
            <slot name="footer">子组件内容：footer插槽中原有的内容</slot>
        </footer>
        </div>
    </div>
</template>