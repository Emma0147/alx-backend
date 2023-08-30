import { describe, it } from 'mocha';
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 12345 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    let error;

    try {
      createPushNotificationsJobs({}, queue);
    } catch (err) {
      error = err;
    }

    expect(error).to.exist;
    expect(error.message).to.equal('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    createPushNotificationsJobs(list, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.eql(list[0]);
    expect(queue.testMode.jobs[1].data).to.eql(list[1]);
  });
});
