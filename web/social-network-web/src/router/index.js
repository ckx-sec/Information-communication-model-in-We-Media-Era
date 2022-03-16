import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */

export const baseRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/login'),
    hidden: true
  },

  {
    path: '/register',
    component: () => import('@/views/login/register'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  }
]

export const suAdminRoutes = [

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '主页', icon: 'dashboard' }
    }]
  },
  {
    path: '/admin/userMgr',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'userMgr',
        component: () => import('@/views/admin/user-mgr'),
        meta: { title: '用户管理', icon: 'user' }
      }
    ]
  },
  {
    path: '/admin/MessageMgr',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'MsgMgr',
        component: () => import('@/views/admin/msg-mgr'),
        meta: { title: '新闻类别', icon: 'el-icon-s-management' }
      }
    ]
  },
  {
    path: '/admin/InitSetup',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'InitSetup',
        component: () => import('@/views/admin/init-setup'),
        meta: { title: '初始设置', icon: 'el-icon-s-help' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: baseRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
