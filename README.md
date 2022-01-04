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
(https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/with-s3-tutorial.html)
(https://dev.classmethod.jp/articles/cloudformation-s3-put-event/)
(https://aws.amazon.com/jp/premiumsupport/knowledge-center/cloudformation-s3-notification-config/)

### 注意点
- Lambdaは別のLambdaを呼ぶ際にネットワークを経由する必要がある
(https://qiita.com/duplicate1984/items/791b13354d9657e7869e)
(https://www.webdevqa.jp.net/ja/amazon-web-services/aws-lambda-invoke%E3%81%8C%E5%88%A5%E3%81%AE%E3%83%A9%E3%83%A0%E3%83%80%E9%96%A2%E6%95%B0%E3%82%92%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%95%E3%81%AA%E3%81%84nodejs/826932732/)
(https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/configuration-vpc.html)

