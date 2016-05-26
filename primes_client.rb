require "bunny"

read_queue_name = ARGV[0]
write_queue_name = ARGV[1]
primes_to_consume = ARGV[2]

connection = Bunny.new
connection.start

channel = connection.create_channel

read_queue = channel.queue(read_queue_name)
write_queue = channel.queue(write_queue_name)

# Ask to the server the amount of numbers we want
write_queue.publish(primes_to_consume)

primes_to_consume.to_i.times do
  while true do
    _delivery_info, _metadata, payload = read_queue.pop
    if !!payload
      puts payload
      break
    end
  end
end

connection.stop
