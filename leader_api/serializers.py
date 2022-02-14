from django.contrib.auth import password_validation
from rest_framework import serializers
from leader.models import Leader
from rest_framework import request
from django.contrib.auth.models import User


class LeaderSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['name', 'text']


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'name', 'text', 'leader_status',]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        leader_ = Leader.objects.create(name=validated_data['name'], text=validated_data['text'],
                                        leader_status=validated_data['leader_status'], owner=user)
        leader_.save()
        return leader_


class UserSerializer(serializers.Serializer):
    username = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

    def create(self, validated_data):
        try:
            password_validation.validate_password(validated_data['password'])
        except:
            raise serializers.ValidationError('Пароль должен состоять из 8 символов. Содержать одну цифру и букву')


        try:
            user = User.objects.create(username=validated_data['username'], password=validated_data['password'])
            user.set_password(validated_data['password'])
            user.save()
        except:
            raise serializers.ValidationError('С данной почтой пользователь зарегистрирован')
        return user
