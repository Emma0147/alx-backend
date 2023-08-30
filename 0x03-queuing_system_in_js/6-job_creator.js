import kue from "kue";

const queue = kue.createQueue();

const notificationData = {
  phoneNumber: "777777777775",
  message: "This is the code to verify your account",
};

const queueName = "push_notification_code";

const notificationJob = queue.create(queueName, notificationData).save((err) => {
  if (!err) console.log(`Notification job created: ${notificationJob.id}`);
});

notificationJob.on("complete", () => {
  console.log("Notification job completed");
});

notificationJob.on("failed", () => {
  console.log("Notification job failed");
});
