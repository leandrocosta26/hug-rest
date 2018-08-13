import hug

import api.resources.user as user

router = hug.route.API(__name__)
router.get('/users', output=hug.output_format.json)(user.get_all_users)
router.get('/user/{_id}', output=hug.output_format.json)(user.get_user_by_id)
router.delete('/user/{_id}')(user.remove_user)
router.put('/user/{_id}')(user.update_user)
router.post('/users')(user.create_user)
