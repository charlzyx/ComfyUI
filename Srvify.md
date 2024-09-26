# /app

## user_manager

- GET /users [获取用户信息]
- POST /users [修改用户信息]
- GET /userdata [用户数据]
- GET /userdata/{file} [用户数据(指定文件)]
- POST /userdata/{file} [更新用户数据]
- DELETE /userdata/{file} [删除用户数据]
- POST /userdata/{file}/move/{dest} [移动用户数据]

## app_settings

- GET /settings
- GET /settings/{id}
- POST /settings
- POST /settings/{id}

# /server

> $client_id

- ws://binary (jpeg/png/json) [中间步骤预览/进度条]
- POST /upload/image [上传图片]
- POST /upload/mask [上传蒙版]
  > 转换为获取 AlphaA 通道
- GET /history [获取历史]
- GET /history/{prompt_id} [获取指定历史]
- GET /prompt [获取当前任务信息]
- POST /prompt [添加任务队列]
- GET /queue [获取队列中当前任务]
- POST /queue [删除/清空队列]
- POST /interrupt [中断任务]

## custome nodes

LoadImage(uploadToOss)
SaveImage(SaveToOss)
