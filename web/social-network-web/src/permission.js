import router from './router'
import { suAdminRoutes } from './router'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style
import getPageTitle from '@/utils/get-page-title'
import Cookies from 'js-cookie'

NProgress.configure({ showSpinner: false }) // NProgress Configuration

const whiteList = ['/login', '/register'] // no redirect whitelist
router.beforeEach(async (to, from, next) => {
  // start progress bar
  NProgress.start()

  // set page title
  document.title = getPageTitle(to.meta.title)

  // determine whether the user has logged in
  // const hasToken = getToken()
  const hasToken = Cookies.get('type')

  // var hasToken = true

  if (hasToken) {
    if (to.path === '/login') {
      next({ path: '/' })
      NProgress.done()
    } else {
      console.log('get options', router.options)

      if (router.options.routes.length === 3) {
        router.addRoutes(suAdminRoutes)
        router.options.routes = router.options.routes.concat(suAdminRoutes)
        console.log(router.options.routes)
        next({ ...to, replace: true })
      }
      next()
    }
  } else {
    /* has no token*/
    // router.addRoutes(baseRoutes)
    // router.options.routes = baseRoutes
    // router.options.routes = router.options.routes.concat(baseRoutes)
    if (whiteList.indexOf(to.path) !== -1) {
      // in the free login whitelist, go directly
      next()
    } else {
      // other pages that do not have permission to access are redirected to the login page.
      next(`/login?redirect=${to.path}`)
      // Message.error({
      //   message: '未登录',
      //   duration: 1500 })
      // NProgress.done()
    }
  }
})

router.afterEach(() => {
  // finish progress bar
  NProgress.done()
})
