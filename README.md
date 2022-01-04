# aws-sample-202111

## ローカル開発
### コマンド
sam local start-api

## デプロイ
1. ビルド
- sam build

2. 初回デプロイ
- sam deploy --guided --capabilities CAPABILITY_IAM

3. デプロイ
- sam deploy

## git-secretsの緩和
https://qiita.com/km1994/questions/9c45923312a654a87685
- 例
  - git config --add secrets.allowed 123456789012

## スタック削除
aws cloudformation delete-stack --stack-name aws-sample-202111 --region ap-northeast-1


## スタック名
lambda-s3-trigger-sample

### 参考
1. CFnでS3トリガー通知設定実装
[https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/with-s3-tutorial.html:title]
[https://dev.classmethod.jp/articles/cloudformation-s3-put-event/:title]
[https://aws.amazon.com/jp/premiumsupport/knowledge-center/cloudformation-s3-notification-config/:title]


