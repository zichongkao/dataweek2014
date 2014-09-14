require 'sinatra'

get '/server' do
  erb :server
end

get '/client' do
  @uuid = Time.now.to_i
  erb :client
end
